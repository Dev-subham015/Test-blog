
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, Comment
from django.http import HttpResponse
from django.contrib import messages



def home(request):
    blog_posts = BlogPost.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {
      'blog_posts': blog_posts, 'categories': categories})

# views.py



from django.utils import timezone
from .models import Contact  # Assuming your Contact model is defined in models.py

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create Contact instance and save to database
        contact = Contact(email=email, subject=subject, message=message, sent_at=timezone.now())
        contact.save()
        
        # Return a success message or redirect to a thank you page
        messages.success(request, "Thank You for contact us")
         
    
    # Handle GET requests or other methods if necessary
    return render(request, 'contact.html')








from django.http import HttpResponseRedirect
from django.urls import reverse


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    # Handle comment submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        # Create and save the comment
        comment = Comment(post=post, name=name, email=email, content=content)
        comment.save()

        # Redirect back to the same page after comment submission
        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))

    # Render the template with blog post and comments
    return render(request, 'blog_detail.html', {'post': post})






def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = BlogPost.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})
