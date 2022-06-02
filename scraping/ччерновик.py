def resume_create:
    user=request.user
    queryset=Resume()
    if request.method == 'POST':
        form= resume_form(request.POST or None)
 
           
        email=user.email

        name=request.POST['name']

        about_meu=request.POST['about_meu']
        adress=request.POST['adress']
        education=request.POST['education']
        phone_number=request.POST['phone_number']
        profession=request.POST['profession']
        skills=request.POST['skills']
        telegram_link=request.POST['telegram_link']
        linked=request.POST['linked']
        res=Resume(email=email,name=name,about_meu=about_meu,adress=adress,education=education,
                   phone_number=phone_number,profession=profession,skills=skills,telegram_link=telegram_link,
                   linked=linked)
        res.save()

        return HttpResponseRedirect(reverse('scraping:resume'))







    else:

        form= resume_form()
    context = {'form': form}

    return render(request, 'accounts/resume_create.html', context)