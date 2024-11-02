import qrcode

# Replace with the link to your deployed Vercel site
url = "https://muhento.github.io/qrinfo/"  # Use the actual URL provided by Vercel

# Generate the QR code
qr = qrcode.make(url)

# Save the QR code as an image file
qr.save("myqr.png")

print("QR code with website link generated and saved as 'my-qr.png'")



