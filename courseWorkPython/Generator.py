import os
import shutil
import subprocess

from GeneratorBMD import GeneratorBMD
from GeneratorU import GeneratorU
from GeneratorVert import GeneratorVert

def recursive_delete(folder):
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
        os.rmdir(folder)


def run_shell():
    current_directory = os.getcwd()
    print(current_directory)
    bash_script_path = os.path.join(current_directory, "Run.sh")
    print(bash_script_path)

    if os.path.isfile(bash_script_path):
        try:
            subprocess.run(["bash", bash_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта: {e}")
    else:
        print("Файл Run.sh не найден в текущем каталоге.")



def generator(l, h, d, lc, rc):
    generatorBMD = GeneratorBMD()
    generatorVert = GeneratorVert(l, h, d, lc, rc)
    generatorVert.generator_vertices()
    generatorVert.generator_edges()
    generatorBMD.export_block_mesh_dict(generatorVert.points_to_string(), generatorVert.edges_to_string())
    generatorU = GeneratorU()
    generatorU.export_u(0.4)

    for i in range(11):
        for j in range(11):
            x = i + j / 10
            if j == 0 and i != 0:
                folder_path = f"{x:.0f}"
            else:
                folder_path = f"{x:.1f}"
            recursive_delete(folder_path)

    print("Complete rm")

    run_shell()
    