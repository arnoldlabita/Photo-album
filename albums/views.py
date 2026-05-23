from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Album, Photo


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')