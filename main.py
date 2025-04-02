import matplotlib.pyplot as plt
print(plt.style.available)
from matplotlib.patches import Polygon, Circle, Rectangle, Ellipse

def draw_coloring_nature_scene():
    # 스타일 설정
    plt.style.use('seaborn-v0_8-pastel')

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 산 그리기 (두 개의 산)
    mountain1 = Polygon([[1, 2], [3, 6], [5, 2]], closed=True, fill=False, edgecolor='black', linewidth=2)
    mountain2 = Polygon([[4, 2], [6, 5], [8, 2]], closed=True, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(mountain1)
    ax.add_patch(mountain2)
    
    # 해 그리기 (원)
    sun = Circle((7, 7), 1, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(sun)
    
    # 나무 그리기 (나무 줄기와 잎)
    tree_trunk = Rectangle((2, 2), 0.5, 2, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(tree_trunk)
    tree_leaves = Polygon([[1.75, 4], [2.25, 5.5], [2.75, 4]], closed=True, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(tree_leaves)
    
    # 구름 그리기 (타원)
    cloud = Ellipse((4, 8), width=3, height=1, angle=0, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(cloud)
    
    # 플롯 설정
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 레이아웃 조정
    fig.tight_layout()
    plt.show()

draw_coloring_nature_scene()