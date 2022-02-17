from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Comment
from .forms import PostModelForm, PostForm, CommentModelForm

# 댓글승인
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.approve()
    return redirect('post_detail', pk=post_pk)

# 댓글삭제
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

# 댓글등록
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 새로 등록하는 comment가 참조하는 post 객체를 저장
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()

    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# 글삭제
@login_required
def post_remove(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list_home')

# 글수정(ModelForm) 사용
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            # form 객체의 save() 호출하면 Model 객체가 생성되어진다.
            post = form.save(commit=False)
            # 로그인된 username을 작성자(author)필드에 저장
            post.author = request.user
            # 현재날짜시간을 게시일자(published_date) 필드에 저장
            post.published_date = timezone.now()
            # post 객체가 저장되면서 insert 처리가 되어진다.
            post.save()
            # 등록 후에 상세페이지로 리다이렉션 처리하기
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'postform': form})

# 글등록(Form) 사용
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # 검증을 통과한 입력 데이터
            print(form.cleaned_data)
            clean_data_dict = form.cleaned_data
            # create() 함수가 호출되면 등록처리가 이루어진다.
            post = Post.objects.create(
                author=request.user,
                title = clean_data_dict['title'],
                text=clean_data_dict['text'],
                published_date=timezone.now()
            )
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'postform': form})

# 글등록 (ModelForm 사용)
@login_required
def post_new_modelform(request):
    if request.method == 'POST':
        # 등록을 요청하는 경우
        post_form = PostModelForm(request.POST)
        # 검증로직을 통과하면
        if post_form.is_valid():
            # form 객체의 save() 호출하면 Model 객체가 생성되어진다.
            post = post_form.save(commit=False)
            # 로그인된 username을 작성자(author)필드에 저장
            post.author = request.user
            # 현재날짜시간을 게시일자(published_date) 필드에 저장
            post.published_date = timezone.now()
            # post 객체가 저장되면서 insert 처리가 되어진다.
            post.save()
            # 등록 후에 상세페이지로 리다이렉션 처리하기
            return redirect('post_detail', pk=post.pk)
    else:
        # 등록을 위한 Form을 출력하는 경우
        post_form = PostModelForm()
    return render(request, 'blog/post_edit.html', {'postform': post_form})

# 글상세정보
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post_key': post})

# 글목록 Pagination
def post_list(request):
    post_queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # Paginator 객체생성
    paginator = Paginator(post_queryset, 2)

    try:
        # page number(페이지번호)를 화면에서 쿼리스트링으로 전달받는다
        page_number = request.GET.get('page')
        # 전달받은 페이지번호로 Page객체생성
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'post_list': page})


# Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체를 Django가 전달해준다.
# 글목록
def post_list_first(request):
    my_name = '장고웹프레임워크'
    http_method = request.method

    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http headers User-Agent : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path))

    # return render(request, 'blog/post_list.html')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})