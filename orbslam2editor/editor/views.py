from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .read_csv import CSVFileReader
from .read_video import VIDEOFileReader


# Create your views here.
def open_editor(request):
    form = choose_file(request)     # uploaded_file = form.cleaned_data['file']
    if form.is_valid():
        csv_file = CSVFileReader(request)
        video_file = VIDEOFileReader(request)
        print("len(video_file.video_data) = ",len(video_file.video_data))
        print("len(csv_file.feature_data) = ",len(csv_file.feature_data))
        print("len(csv_file.world_data) = ",len(csv_file.world_data))
        request.session['video_data'] = video_file.video_data
        request.session['feature_data'] = csv_file.feature_data
        request.session['world_data'] = csv_file.world_data
        

        return redirect('start_editor/')
        # return render(request, 'test.html', {'form': form, 'csv_file': csv_file, 'video_file': video_file})
    return render(request, 'test.html', {'form': form})

def choose_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("處理表單驗證成功")
        else:
            print("處理表單驗證錯誤")
    else:
        form = FileUploadForm()
    return form

def start_editor(request):
    # csv_file = request.GET.get('csv_file', None)
    # video_file = request.GET.get('video_file', None)
    video_data = request.session.get('video_data', None)
    feature_data = request.session.get('feature_data', None)
    world_data = request.session.get('world_data', None)
    return render(request, 'starteditor.html', { 'video_data': video_data, 'feature_data': feature_data, 'world_data': world_data})

