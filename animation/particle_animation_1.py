import numpy as np 
import open3d as o3d 
import copy


if __name__ == "__main__":
    origin = o3d.geometry.TriangleMesh.create_coordinate_frame()

    T = np.eye(4)
    floor = o3d.geometry.TriangleMesh.create_box(width=7, height=3, depth=0.1)
    floor.compute_vertex_normals()
    floor.paint_uniform_color([1, 1, 1])
    floor.translate((0, 0, -0.1), relative=True)

    side_wall_1 = o3d.geometry.TriangleMesh.create_box(width=1.5, height=0.25, depth=0.5)
    side_wall_1.compute_vertex_normals()
    side_wall_1.paint_uniform_color([0.5, 0.5, 0.5])

    side_wall_2 = copy.deepcopy(side_wall_1).translate((0, 2.75, 0), relative=True)

    back_wall = o3d.geometry.TriangleMesh.create_box(width=3, height=0.25, depth=0.5)
    back_wall.compute_vertex_normals()
    back_wall.paint_uniform_color([0.5, 0.5, 0.5])
    R = origin.get_rotation_matrix_from_xyz((0, 0, np.pi / 2))
    back_wall.rotate(R, center=(0, 0, 0))

    cylinder_object = o3d.geometry.TriangleMesh.create_cylinder(radius=0.5, height=0.5)
    cylinder_object.compute_vertex_normals()
    cylinder_object.paint_uniform_color([0.5, 0.5, 0.0])
    cylinder_object.translate((3, 1.5, 0))

    sphere_object = o3d.geometry.TriangleMesh.create_sphere(radius = 0.1)
    sphere_object.compute_vertex_normals()
    sphere_object.paint_uniform_color([1, 0.706, 0])
    sphere_object.translate((0.5, 1.5, 0.1))

    exit_wall_1 = o3d.geometry.TriangleMesh.create_box(width=1.25, height=0.25, depth=0.5)
    exit_wall_1.compute_vertex_normals()
    exit_wall_1.paint_uniform_color([0.5, 0.5, 0.5])
    R = origin.get_rotation_matrix_from_xyz((0, 0, np.pi / 2))
    exit_wall_1.rotate(R, center=(0, 0, 0))
    exit_wall_1.translate((4.5, 0, 0))

    exit_wall_2 = copy.deepcopy(exit_wall_1).translate((0, 1.75, 0))

    o3d.visualization.draw_geometries([origin, floor, side_wall_1, side_wall_2, back_wall, cylinder_object, sphere_object, exit_wall_1, exit_wall_2])

    print('end')



