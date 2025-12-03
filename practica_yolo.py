from ultralytics import YOLO

def main():
    model = YOLO("yolo11m.pt")

    imagenes = [
        "1.jpg",
        "2.jpg",
        "3.jpg"
    ]

    resultados = model.predict(
        source=imagenes,
        save=True,
        conf=0.25
    )

    for i, r in enumerate(resultados):
        print(f"\n🔹 RESULTADOS PARA: {imagenes[i]}")
        for cls_id, conf in zip(r.boxes.cls, r.boxes.conf):
            nombre_clase = r.names[int(cls_id)]
            print(f"  - {nombre_clase} (confianza: {float(conf):.2f})")

if __name__ == "__main__":
    main()
