export function get(endpoint) {
    return axios.get(HOST + endpoint)
}

export function set(endpoint, body, isJson = false) {
    let options = {}
    
    if(isJson) {
        options.headers = {'Content-Type': "application/json"};
    }
    
    return axios.put(HOST + endpoint, body, options = options)
}

export function create(endpoint, body) {
    return axios.post(HOST + endpoint, body)
}