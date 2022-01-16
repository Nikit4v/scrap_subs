import pathlib
import subprocess
import shutil
import sys

from tqdm import tqdm

working_path = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(".")


processes = []
for mkv in tqdm(working_path.glob('**/*.mkv'), total=len(list(working_path.glob('**/*.mkv')))):
    new_path = pathlib.Path('./scrapped') / (str(mkv)[:-3]+'ass')
    new_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.Popen(['C:\Program Files\ffmpeg\bin\ffmpeg.exe', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(mkv.absolute()), '-map', '0:s:0', str(new_path)], stdout=subprocess.DEVNULL).wait()

shutil.make_archive("SENDME", 'zip', pathlib.Path('./scrapped').absolute().__str__())

shutil.rmtree(pathlib.Path("./scrapped"))

print("Finished!")
print("File SENDME.zip contains all subtitles.")
