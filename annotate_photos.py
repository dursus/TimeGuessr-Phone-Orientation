import cv2
import os
import glob

# Configuration
INPUT_DIR = "images"       
OUTPUT_DIR = "annotated"   

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors in BGR format:
# Blue (Horizontal), Coral (Vertical), White (Ambiguous/Digital Camera)
COLORS = {
    'b': ((255, 0, 0), "Blue - Horizontal"),
    'c': ((76, 104, 235), "Coral - Vertical"), 
    'w': ((200, 200, 200), "White - Ambiguous/Camera")
}

current_color_key = 'b'
drawing = False
ix, iy = -1, -1
boxes = [] 

def draw_preview(img_copy):
    for box in boxes:
        cv2.rectangle(img_copy, (box[0], box[1]), (box[2], box[3]), box[4], 2)
    color_name = COLORS[current_color_key][1]
    cv2.putText(img_copy, f"Mode: {color_name} | Keys: [b]lu, [c]or, [e]wh, [u]ndo, [n]ext, [q]uit", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLORS[current_color_key][0], 2)
    return img_copy

def mouse_callback(event, x, y, flags, param):
    global drawing, ix, iy, boxes, img_display, img_original
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img_original.copy()
            for box in boxes:
                cv2.rectangle(img_copy, (box[0], box[1]), (box[2], box[3]), box[4], 2)
            cv2.rectangle(img_copy, (ix, iy), (x, y), COLORS[current_color_key][0], 2)
            img_display = draw_preview(img_copy)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)
        if abs(x2 - x1) > 5 and abs(y2 - y1) > 5:
            boxes.append((x1, y1, x2, y2, COLORS[current_color_key][0], current_color_key))
        img_display = draw_preview(img_original.copy())

image_paths = sorted(glob.glob(os.path.join(INPUT_DIR, "*.*")))
if not image_paths:
    print(f"No images found in '{INPUT_DIR}' folder! Please add your images there first.")
    exit()

print("--- Annotation Tool Active ---")
print("Controls:")
print("  - Click and drag: Draw box")
print("  - Press 'b': Switch to Blue (Horizontal)")
print("  - Press 'c': Switch to Coral (Vertical)")
print("  - Press 'w': Switch to White (Ambiguous/Camera)")
print("  - Press 'u': Undo last box")
print("  - Press 'n': Save and go to next image")
print("  - Press 'q': Quit")

for path in image_paths:
    img_original_full = cv2.imread(path)
    if img_original_full is None:
        continue
        
    h_orig, w_orig = img_original_full.shape[:2]
    
    # Scale down for large images so they fit nicely on your screen
    max_dim = 900
    scale = 1.0
    if max(h_orig, w_orig) > max_dim:
        scale = max_dim / max(h_orig, w_orig)
        img_original = cv2.resize(img_original_full, (int(w_orig * scale), int(h_orig * scale)))
    else:
        img_original = img_original_full.copy()
        
    img_display = img_original.copy()
    boxes = []
    
    window_name = f"Annotating: {os.path.basename(path)}"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)
    
    img_display = draw_preview(img_display.copy())
    
    skip_rest = False
    while True:
        cv2.imshow(window_name, img_display)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit()
        elif key == ord('n'):
            # Map boxes back to original full resolution image scale before saving
            final_save = img_original_full.copy()
            for box in boxes:
                fx1, fy1 = int(box[0] / scale), int(box[1] / scale)
                fx2, fy2 = int(box[2] / scale), int(box[3] / scale)
                cv2.rectangle(final_save, (fx1, fy1), (fx2, fy2), box[4], max(3, int(4/scale)))
                
            out_path = os.path.join(OUTPUT_DIR, os.path.basename(path))
            cv2.imwrite(out_path, final_save)
            print(f"Saved: {out_path}")
            break
        elif key == ord('b'):
            current_color_key = 'b'
            img_display = draw_preview(img_original.copy())
        elif key == ord('c'):
            current_color_key = 'c'
            img_display = draw_preview(img_original.copy())
        elif key == ord('w'):
            current_color_key = 'w'
            img_display = draw_preview(img_original.copy())
        elif key == ord('u'):
            if boxes:
                boxes.pop()
                img_display = draw_preview(img_original.copy())
                
    cv2.destroyWindow(window_name)

print("All images processed successfully!")