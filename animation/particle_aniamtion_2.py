import numpy as np 
import open3d as o3d 
import copy



if __name__ == "__main__":
    origin = o3d.geometry.TriangleMesh.create_coordinate_frame()
    T = np.eye(4)
    floor = o3d.geometry.TriangleMesh.create_box(width=4, height=4, depth=0.1)
    floor.compute_vertex_normals()
    floor.paint_uniform_color([1, 1, 1])
    floor.translate((0, 0, -0.1), relative=True)

    box_1 = o3d.geometry.TriangleMesh.create_box(width=4, height=1, depth=0.5)
    box_1.compute_vertex_normals()
    box_1.paint_uniform_color([0.5, 0.5, 0.5])

    box_2 = o3d.geometry.TriangleMesh.create_box(width=1.5, height=2, depth=0.5)
    box_2.compute_vertex_normals()
    box_2.paint_uniform_color([0.5, 0.5, 0.5])
    box_2.translate((0, 2, 0), relative=True)

    box_3 = copy.deepcopy(box_2).translate((2.5, 0, 0), relative=True)

    top_sphere_object = o3d.geometry.TriangleMesh.create_sphere(radius = 0.1)
    top_sphere_object.compute_vertex_normals()
    top_sphere_object.paint_uniform_color([0.1, 0.1, 0.7])
    top_sphere_object.translate((2, 3.7, 0.1))

    side_sphere_object = o3d.geometry.TriangleMesh.create_sphere(radius = 0.1)
    side_sphere_object.compute_vertex_normals()
    side_sphere_object.paint_uniform_color([1, 0.706, 0])
    side_sphere_object.translate((3.7, 1.5, 0.1))

    o3d.visualization.draw_geometries([origin, floor, box_1, box_2, box_3, top_sphere_object, side_sphere_object], 
                                      zoom=0.0, front=[0.4257, -0.2125, -0.8795], lookat=[2.6172, 2.0475, 1.532], up=[-0.0694, -0.9768, 0.2024])

    print('end')



