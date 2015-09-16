from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
import json

def template_two(request):
    view = "template_two"
    t = get_template("my_view.html")
    html = t.render(Context({'name': view}))
    return HttpResponse(html)


def resume(request):
    view = "resume"
    return render_to_response("resume.html", {"name": view})


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 10)
    return render_to_response('articles.html',
                              {'articles': current_page.page(page_number), "username": auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args["article"] = Article.objects.get(id=article_id)
    args["comments"] = Comments.objects.filter(comments_article_id=article_id)
    args["form"] = comment_form
    args["username"] = auth.get_user(request).username
    return render_to_response("article.html", args)


def add_like(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect("/")
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect("/")
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect("/")


def add_comment(request, article_id):
    if request.method == "POST":
        post_text = request.POST.get('the_post')
        response_data = {'text': post_text}

        post = Comments(comments_text=post_text, comments_article=Article.objects.get(id=article_id))
        post.save()

        return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )