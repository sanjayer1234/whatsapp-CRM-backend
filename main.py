from fastapi import FastAPI, Request, HTTPException
import traceback

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "WhatsApp CRM backend is running!"}

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    try:
        # Extract form data from the webhook request
        form_data = await request.form()
        message_data = dict(form_data)

        print("✅ Incoming WhatsApp Message:")
        for key, value in message_data.items():
            print(f"{key}: {value}")

        # You can now later store this in MongoDB or process further
        return {"status": "received"}

    except Exception as e:
        print("❌ Error processing webhook:")
        traceback.print_exc()  # Print detailed error to terminal
        raise HTTPException(status_code=500, detail="Failed to process request")
