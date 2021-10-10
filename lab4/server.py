from waitress import serve
import lab4


if __name__ == "__main__":
    serve(lab4.lab4, host='0.0.0.0', port=5000)