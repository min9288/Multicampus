from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostModelForm, PostForm

# 글등록(Form) 사용
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            clean_data_dict = form.cleaned_data
            # create() 함수가 호출되면 등록처리가 이루어진다.
            post = Post.objects.create(
                author=request.user,
                title=clean_data_dict['title'],
                text = clean_data_dict['text'],
                published_date=timezone.now()
            )
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'postform':form})

# 글등록
def post_new_modelform(request):
    if request.method == 'POST':
        # 등록을 요청하는 경우
        post_form = PostModelForm(request.POST)
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

# 글 상세정보
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post_key': post})


# View 내에 선언된 함수로 인자로 HttpRequest 하는 객체를 Django가 전달해준다.
# 글 목록
def post_list(request):
    my_name = '장고웹프레임워크'
    http_method = request.method

    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http headers User-Agent : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path))

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})
