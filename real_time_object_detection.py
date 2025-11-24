#!/usr/bin/env python3


# Open source
cap = open_video_source(args.source)


# Warm up variables for FPS calculation
fps = 0.0
frame_count = 0
start_time = time.time()


try:
while True:
ret, frame = cap.read()
if not ret:
print("End of stream or cannot fetch frame.")
break


frame = resize_keep_aspect(frame, width=args.width)
(h, w) = frame.shape[:2]


# Prepare blob and perform forward pass
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()


# Loop over detections
for i in range(0, detections.shape[2]):
confidence = float(detections[0, 0, i, 2])
if confidence < args.conf:
continue


idx = int(detections[0, 0, i, 1])
box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
(startX, startY, endX, endY) = box.astype("int")


label = CLASSES[idx] if idx < len(CLASSES) else f"Class #{idx}"
text = f"{label}: {confidence:.2f}"


# Draw bounding box and label
color = COLORS[idx]
cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
y = startY - 15 if startY - 15 > 15 else startY + 15
cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)


# Compute FPS
frame_count += 1
elapsed = time.time() - start_time
if elapsed >= 1.0:
fps = frame_count / elapsed
frame_count = 0
start_time = time.time()


# Overlay FPS
cv2.putText(frame, f"FPS: {fps:.2f}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


# Display
cv2.imshow("Real-Time Object Detection", frame)


# Press 'q' or ESC to quit
key = cv2.waitKey(1) & 0xFF
if key == ord('q') or key == 27:
break


except KeyboardInterrupt:
print("Interrupted by user")
finally:
cap.release()
cv2.destroyAllWindows()




if __name__ == "__main__":
main()
