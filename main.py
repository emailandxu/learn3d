from zipfile import ZipFile
with ZipFile("bunny.zip") as myzip:
    with myzip.open("bunny.obj", "r") as f:
        with open("bunny.obj", "wb") as outf:
            outf.write(f.read())


import trimesh
import polyscope as ps


mesh = trimesh.load("bunny.obj")

v, f = mesh.vertices, mesh.faces

ps.init()
ps.register_point_cloud("my_points", v)
ps.register_surface_mesh("my_face", f)
ps.show()