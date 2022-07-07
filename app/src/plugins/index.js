import Toast from './toast/Toast'

export default {
    install(Vue){
        const commponent = Vue.extend(Toast)
        const newToast = new commponent()
        document.body.appendChild(newToast.$mount().$el)
        Vue.prototype.$toast = {
            success(text){
                newToast.text = text
                newToast.type = 'success'
                newToast.isShow = true
                const id = setTimeout(()=>{
                    newToast.isShow = false
                    clearTimeout(id)
                }, 2000)
            },
            error(text){
                newToast.text = text
                newToast.type = 'error'
                newToast.isShow = true
                const id = setTimeout(()=>{
                    newToast.isShow = false
                    clearTimeout(id)
                }, 2000)
            },
            warning(text){
                newToast.text = text
                newToast.type = 'warning'
                newToast.isShow = true
                const id = setTimeout(()=>{
                    newToast.isShow = false
                    clearTimeout(id)
                }, 2000)
            }
        }
    }
}