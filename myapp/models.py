from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, max_length=10)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True, max_length=10)
    movie_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    start_date = models.DateTimeField
    end_date = models.DateTimeField


class Show(models.Model):
    show_id = models.IntegerField(primary_key=True, max_length=10)
    show_date = models.DateTimeField
    show_time = models.DateTimeField
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Hall(models.Model):
    hall_id = models.IntegerField(primary_key=True, max_length=10)
    no_of_seats = models.IntegerField(max_length=5)
    available_seats = models.IntegerField(max_length=5)


class Seat(models.Model):
    seat_id = models.IntegerField(primary_key=True, max_length=10)
    availability = models.BooleanField


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True, max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True, max_length=10)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    method = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=5)
