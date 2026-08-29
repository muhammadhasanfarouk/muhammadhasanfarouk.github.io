from PIL import Image

def dither_image(input_path, output_path):
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Resize slightly if it's too large to make the dithering dots more visible
        # (Pixelated effect looks better if the base image has lower resolution)
        max_size = (400, 400)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to grayscale
        img = img.convert("L")
        
        # Convert to 1-bit pixels, black and white, with Floyd-Steinberg dithering
        img = img.convert("1", dither=Image.FLOYDSTEINBERG)
        
        # Convert back to RGBA to make black transparent
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # item is (R, G, B, A). In "1" converted to "RGBA", B&W is (0,0,0,255) and (255,255,255,255)
            if item[0] == 0:
                newData.append((0, 0, 0, 0)) # transparent black
            else:
                newData.append((255, 255, 255, 200)) # slightly transparent white for the dots
                
        img.putdata(newData)
        
        # Save the result
        img.save(output_path, "PNG")
        print(f"Successfully dithered and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

dither_image(r"c:\Users\moham\Codes\Git\muhammadhasanfarouk.github.io\images\profile.jpg", r"c:\Users\moham\Codes\Git\muhammadhasanfarouk.github.io\images\profile_dithered.png")
