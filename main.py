import animator
import lorenz

if __name__ == '__main__':
    animator.Animator(
        title = "Lorenz Attractor",
        limit = 50000, 
        generators = [lorenz.attractor()]).animate()