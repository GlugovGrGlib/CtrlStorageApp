def show_stock(request):
    elements_view = models.ElementsBase.objects.all()
    current_user = request.user
    return render_to_response("show_stock.html", locals())
