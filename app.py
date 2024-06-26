from flask import Flask, render_template, request, redirect, url_for
import etcd3

# Initialize Flask app
app = Flask(__name__)

# Initialize etcd client
etcd = etcd3.client()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/put', methods=['POST'])
def put():
    key = request.form['key']
    value = request.form['value']
    etcd.put(key, value)
    return redirect(url_for('index'))

@app.route('/get', methods=['POST'])
def get():
    key = request.form['key']
    try:
        value, _ = etcd.get(key)
        if value is not None:
            result = f"Value for key '{key}': {value.decode()}"
        else:
            result = f"Key '{key}' not found"
    except etcd3.exceptions.ConnectionFailedError:
        result = "Error: Connection to etcd cluster failed."
    except Exception as e:
        result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']
    try:
        value, _ = etcd.get(key)
        if value is not None:
            etcd.delete(key)
            result = f"Key '{key}' successfully deleted"
        else:
            result = f"Key '{key}' does not exist"
    except etcd3.exceptions.ConnectionFailedError:
        result = "Error: Connection to etcd cluster failed."
    except etcd3.exceptions.KeyNotFoundError:
        result = f"Error: Key '{key}' not found."
    except Exception as e:
        result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

# @app.route('/list_all')
# def list_key():
#     try:
#         x = list_keys()
#         # keys = etcd.get_all()
#         # print(keys)
#         # keys_list = [key for key, _ in keys]
#         print(x)
#         return render_template('list.html', keys=x)
#     except etcd3.exceptions.ConnectionFailedError:
#         result = "Error: Connection to etcd cluster failed."
#         return render_template('index.html', result=result)
#     except Exception as e:
#         result = f"Error: {str(e)}"
#         return render_template('index.html', result=result)

def list_keys():
    """List all keys in etcd."""
    return [meta.key.decode() for _, meta in etcd.get_all()]

def dict_all(list_keys):
    key_val={}
    for i in list_keys:
        key_val[i], _ = etcd.get(i)
    return key_val

            
@app.route('/list_all')
def list_all():
    try:
        vals=dict_all(list_keys())
        return render_template('list.html', dct=vals)
    except etcd3.exceptions.ConnectionFailedError:
        result = "Error: Connection to etcd cluster failed."
        return render_template('index.html', result=result)
    except Exception as e:
        result = f"Error: {str(e)}"
        return render_template('index.html', result=result)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    