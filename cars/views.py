from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    # 1. Use the ID from the URL to get the specific car from the database
    single_car = get_object_or_404(Car, pk=id)
    
    # 2. Pass that car data into the template
    data = {
        'single_car': single_car,
    }
    
    # 3. Render the correct template file
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    # Dropdown options for your search forms
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct() # Added drop-down list

    # Keyword Search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

# Model Search
    if 'model' in request.GET:
        model = request.GET['model']
        if model and model != 'Select Model': # Ignore placeholder
            cars = cars.filter(model__iexact=model)

    # City Search
    if 'city' in request.GET:
        city = request.GET['city']
        if city and city != 'Select Location': # Ignore placeholder
            cars = cars.filter(city__iexact=city)

    # Year Search
    if 'year' in request.GET:
        year = request.GET['year']
        if year and year != 'Select Year': # Ignore placeholder
            cars = cars.filter(year__iexact=year)

    # Body Style Search
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style and body_style != 'Select Type Of Car': # Ignore placeholder
            cars = cars.filter(body_style__iexact=body_style)

    # Transmission Search
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission and transmission != 'Transmission': # Ignore placeholder
            cars = cars.filter(transmission__iexact=transmission)
    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search, # Added here for your template
    }
    return render(request, 'cars/search.html', data)