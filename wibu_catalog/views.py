from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.core.paginator import Paginator
from django.utils import timezone

from django.db.models import Q
# import data from constants.py
from wibu_catalog.constants import Role_dict, Score_dict, ITEMS_PER_PAGE_MORE
from wibu_catalog.constants import ITEMS_PER_PAGE, Content_category
from wibu_catalog.constants import Manga_status, Anime_status
from wibu_catalog.constants import Manga_rating, Anime_rating
from wibu_catalog.constants import FIELD_MAX_LENGTH_S, FIELD_MAX_LENGTH_M
from wibu_catalog.constants import FIELD_MAX_LENGTH_L, FIELD_MAX_LENGTH_XL

# import models form models.py
from wibu_catalog.models import Content, Score, Users, FavoriteList
from wibu_catalog.models import ScoreList, Comments, Notifications
from wibu_catalog.models import Product, Order, OrderItems, Feedback

from .constants import TOP_WATCHING_LIMIT, LATEST_CONTENT_LIMIT, TOP_RANKED_LIMIT
from wibu_catalog.constants import ITEMS_PER_PAGE
from django.contrib.auth.hashers import check_password

from django.shortcuts import redirect, render
from .models import Users
from .forms import LoginForm, CommentForm, EditCommentForm
from django.views import View


def _get_user_from_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return Users.objects.get(uid=user_id)
        except Users.DoesNotExist:
            return None
    return None

def homepage(request):
    userr = _get_user_from_session(request)
    top_watching_content = Content.objects.order_by('-watching')[:TOP_WATCHING_LIMIT]

    latest_content = Content.objects.order_by('-lastUpdate')[:LATEST_CONTENT_LIMIT]

    top_ranked_content = Content.objects.order_by('ranked')[:TOP_RANKED_LIMIT]

    return render(request, 'html/homepage.html', {
        'top_watching_content': top_watching_content,
        'latest_content': latest_content,
        'top_ranked_content': top_ranked_content,
        'userr': userr
    })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'html/registerform.html', {'form': form})


# Class definition:
class AnimeListView(generic.ListView):
    """Class for the view of the book list."""
    model = Content
    context_object_name = "anime_list"
    paginate_by = ITEMS_PER_PAGE_MORE
    template_name = "html/anime_list.html"

    def get_queryset(self):
        return Content.objects.filter(category="anime")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anime_list = self.get_queryset()
        userr = _get_user_from_session(self.request)
        context = {"userr":userr, "anime_list":anime_list,}
        return context


class AnimeDetailView(generic.DetailView):
    """Yahalo"""
    model = Content
    context_object_name = "anime_detail" # get overide by get_context_data
    template_name = "html/anime_detail.html"

    # passing Score to view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content_instance = self.get_object()
        score_data_ = content_instance.score_data.all()
        # Auth user if user in User table
        userr = _get_user_from_session(self.request)
        # Get comments for this anime
        comments_list = Comments.objects.filter(cid=content_instance.cid).order_by('-dateOfCmt')
        # Pagination
        paginator = Paginator(comments_list, 5)
        page_number = self.request.GET.get('page')
        comments = paginator.get_page(page_number)
        # Sumarize context
        context = {'score_': score_data_, "userr":userr, "anime_detail":content_instance, "comments":comments}
        return context


class MangaListView(generic.ListView):
    """Class for the view of the book list."""
    model = Content
    paginate_by = ITEMS_PER_PAGE_MORE
    context_object_name = "manga_list"
    template_name = "html/manga_list.html"

    def get_queryset(self):
        return Content.objects.filter(category='manga').all()


class MangaDetailView(generic.DetailView):
    model = Content
    context_object_name = "manga_detail"
    template_name = "html/manga_detail.html"

    # passing Score to view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content_instance = self.get_object()
        score_data_ = content_instance.score_data.all()
        context['score_'] = score_data_
        return context


def list_product(request):
    userr = _get_user_from_session(request)
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL, mặc định là chuỗi rỗng
    sort_by = request.GET.get('sort_by', 'id')  # Giá trị mặc định là 'id'

    # Tìm kiếm sản phẩm theo từ khóa
    if query:
        products_list = Product.objects.filter(name__icontains=query)
    else:
        products_list = Product.objects.all()

    # Sắp xếp sản phẩm theo yêu cầu
    if sort_by == 'highest_rate':
        products_list = products_list.order_by('-ravg')
    elif sort_by == 'low_to_high':
        products_list = products_list.order_by('price')
    elif sort_by == 'high_to_low':
        products_list = products_list.order_by('-price')

    paginator = Paginator(products_list, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'html/warehouse.html', {'products': products, 'current_sort': sort_by, 'query': query,"userr":userr})

def search_content(request):
    query = request.GET.get('q','').lower()
    search_results = None
    if query:
        search_results = Content.objects.filter(name__icontains=query)
    else:
        search_results = Content.objects.all()  # Nếu không có từ khóa, hiển thị tất cả

    return render(request, 'html/search_content_results.html', {'search_results': search_results,})

def filter_by_genre(request, genre):
    userr = _get_user_from_session(request)

    # Lọc content theo thể loại và sắp xếp theo scoreAvg
    filtered_content = Content.objects.filter(genres__icontains=genre).order_by('-scoreAvg')[:ITEMS_PER_PAGE]

    context = {
        'filtered_content': filtered_content,
        'selected_genre': genre,
        'userr': userr
    }
    return render(request, 'html/filtered_content.html', context)



class LoginView(View):
    def _authenticate_user(self, email, password):
        try:
            user = Users.objects.get(email=email)
            if password == user.password:
                return user
            else:
                return None
        except Users.DoesNotExist:
            return None

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = self._authenticate_user(email=email, password=password)
        if user is not None:
            request.session['user_id'] = user.uid
            return redirect('homepage')
        else:
            form = LoginForm()
            return render(request, 'html/loginform.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'html/loginform.html', {'form': form})


def logout(request):
    request.session.flush()
    return redirect('homepage')


# Comment section:
def post_comment(request, content_id):
    userr = _get_user_from_session(request)
    cmtedContent = get_object_or_404(Content, cid=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.cid = cmtedContent
            comment.uid = userr
            comment.dateOfCmt = timezone.now().date()
            comment.save()
            # debuging corner
            print("Comment saved:", comment)  # Debugging line
            print(Comments.objects.filter(uid=userr, cid=cmtedContent))
            return redirect('anime_detail', pk=content_id)
    return redirect('anime_detail', pk=content_id)


def edit_comment(request, comment_id):
    userr = _get_user_from_session(request)
    try:
        comment = Comments.objects.get(id=comment_id, uid=userr.uid)
    except Comments.DoesNotExist:
        print("DEBUG===============================")
        print("FUCK UP AT EDIT COMMENT MY FURIENDO")
        print("DEBUG===============================")
        return redirect('anime_detail', pk=comment.cid.cid)

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.dateOfCmt = timezone.now().date()  # Update the date
            comment.save()
            return redirect('anime_detail', pk=comment.cid.cid)
            # somehow comment.cid = Content.__str__
    else:
        form = EditCommentForm(instance=comment)

    return redirect('anime_detail', pk=comment.cid.cid)


def delete_comment(request, comment_id):
    userr = _get_user_from_session(request)

    try:
        comment = Comments.objects.get(id=comment_id)
        comment.delete()
    except Comments.DoesNotExist:
        print("DEBUG===============================")
        print("FUCK UP AT DEL COMMENT MY FURIENDO")
        print("DEBUG===============================")
        return redirect('anime_detail', pk=comment.cid.cid)
    return redirect('anime_detail', pk=comment.cid.cid)
