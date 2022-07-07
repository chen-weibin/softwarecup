
export const getCookie = (key) => {
    const cookie = document.cookie
    const re = new RegExp(key + '=(\\w+)', 'g')
    const res = cookie.match(re)
    let value = ''
    if (res) {
        value = res[0].split('=')[1]
    }
    return value
}

export const setCookie = (key, value, time=60 * 60 * 24) => { 
    const cookie = `${key}=${value}; max-age=${time}`
    document.cookie = cookie
}



