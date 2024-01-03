from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse , JsonResponse
from account.models import *
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from admins.forms import *
from manager.forms import *
from employee.forms import TaskForm
