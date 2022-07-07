const loginFrame = () => import ('../views/loginFrame')
const home = () => import('../views/home')

const targetExtraction = () => import('../views/targetExtraction')
const changeDetection = () => import('../views/changeDetection')
const targetDetection = () => import('../views/targetDetection')
const terrainClassification = () => import('../views/terrainClassification')

const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        component: home,
    },
    {
        path: '/login',
        component: loginFrame
    },
    {
        path: '/targetextraction',
        component: targetExtraction
    },
    {
        path: '/changedetection',
        component: changeDetection,
    },
    {
        path: '/targetdetection',
        component: targetDetection
    },
    {
        path: '/classification',
        component: terrainClassification
    }
]

export default routes