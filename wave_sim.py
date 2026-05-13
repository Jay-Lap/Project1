import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. 시뮬레이션 설정 (계산 부하를 줄여서 부드럽게 만듦)
grid_size = 100 
dt = 0.1

# 필드 초기화
Ez = np.zeros((grid_size, grid_size))
Hx = np.zeros((grid_size, grid_size))
Hy = np.zeros((grid_size, grid_size))

# 시각화 설정
fig, ax = plt.subplots(figsize=(8, 8), num="Maxwell's Wave Simulation")
# vmin/vmax 범위를 좁혀서 아주 작은 파동도 잘 보이게 설정
im = ax.imshow(Ez, cmap='RdBu', vmin=-0.2, vmax=0.2, interpolation='bilinear')
ax.set_title("Maxwell Wave Propagation (Click the plot if it's stuck)")
fig.colorbar(im)

# 2. 업데이트 함수
def update(frame):
    global Ez, Hx, Hy
    
    # [안테나] 중앙에서 강한 진동 발생
    # frame이 증가함에 따라 사인파가 변하며 파동을 만들어냄
    Ez[50, 50] = np.sin(0.4 * frame)
    
    # 맥스웰 방정식 수치 계산 (FDTD)
    Hx[:, :-1] -= dt * (Ez[:, 1:] - Ez[:, :-1])
    Hy[:-1, :] += dt * (Ez[1:, :] - Ez[:-1, :])
    Ez[1:-1, 1:-1] += dt * (Hy[1:-1, 1:-1] - Hy[:-2, 1:-1] - 
                           Hx[1:-1, 1:-1] + Hx[1:-1, :-2])
    
    # 화면 갱신
    im.set_array(Ez)
    return [im]

# 3. 애니메이션 실행 (blit=False로 설정하여 호환성 높임)
ani = FuncAnimation(fig, update, frames=200, interval=20, blit=False)
plt.show()