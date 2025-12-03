from ultralytics import YOLO

def main():
    # 1. Cargar tu modelo entrenado
    model = YOLO("runs/detect/train2/weights/best.pt")

    # 2. Probarlo con imágenes de validación o nuevas
    resultados = model.predict(
        source="dataset_gatos/images/train/1.jpg",  # pon la imagen que quieras
        save=True,
        conf=0.05
    )

    # 3. Mostrar las predicciones por consola (opcional)
    for r in resultados:
        for cls_id, conf in zip(r.boxes.cls, r.boxes.conf):
            print(f"Clase detectada: {r.names[int(cls_id)]}, confianza: {float(conf):.2f}")

if __name__ == "__main__":
    main()
