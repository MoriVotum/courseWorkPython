import os
import shutil

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


if __name__ == "__main__":
    generatorBMD = GeneratorBMD()
    generatorVert = GeneratorVert(180, 23, 12, 30, 8)
    generatorVert.generator_vertices()
    generatorVert.generator_edges()
    generatorBMD.export_block_mesh_dict(generatorVert.points_to_string(), generatorVert.edges_to_string())
    generatorU = GeneratorU()
    generatorU.export_u(0.41246)

    for i in range(10):
        for j in range(1, 10):
            x = i + j / 10
            folder_path = f"calculate/{x:.1f}"
            recursive_delete(folder_path)

    print("Complete rm")
