import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", port=3000, log_level='debug', reload=True)
