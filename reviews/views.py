from django.shortcuts import render

<<<<<<< Updated upstream
# Create your views here.
=======

def index(request):
    return render(request, "reviews/index.html")


def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:index")
    else:
        form = MovieForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/movie_create.html", context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        "movie": movie,
        "reviews": movie.review_set.all(),
    }
    return render(request, "reviews/movie_detail.html", context)


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("reviews:movie_detail", pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        "form": form,
    }
    return render(request, "reviews/movie_update.html", context)


def review_create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            form = review_form.save(commit=False)
            form.movie = movie
            form.user = request.user
            form.save()
            return redirect("reviews:movie_detail", pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/review_create.html", context)


def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        "review": review,
        "comment_form": CommentForm(),
        "comments": review.comment_set.all(),
    }
    return render(request, "reviews/review_detail.html", context)


def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:review_detail", review.pk)

    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/review_detail.html", context)


def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST" and review.user == request.user:
        review.delete()
    return redirect("reviews:movie_detail", movie_pk)


def comment_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.user = request.user
            form.review = review
            form.save()
            return redirect("reviews:review_detail", review_pk)


def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST" and comment.user == request.user:
        comment.delete()
        return redirect("reviews:review_detail", review_pk)


def like(request):
    pass
>>>>>>> Stashed changes
