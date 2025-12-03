from ultralytics import YOLO


def main():
    # 1. Cargar YOLO preentrenado como base
    model = YOLO("yolo11n.pt")   # puedes usar también yolo11s.pt si quieres

    # 2. Entrenar con tu dataset anotado
    model.train(
        data="dataset_gatos/gatos.yaml",  # ruta al yaml
        epochs=5,                         # pon 3 si quieres más rápido
        imgsz=640,                        # tamaño de imagen
        batch=-1                          # usa batch automático
    )


if __name__ == "__main__":
    main()
