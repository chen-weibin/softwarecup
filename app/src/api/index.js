import axios from 'axios'

// axios 的默认配置
axios.defaults.baseURL = 'http://127.0.0.1:3000' //5000实际
axios.defaults.timeout = 20000

// 请求拦截器
axios.interceptors.request.use(config => {
    return config
}, error => {
    return Promise.reject(error)
})
// 响应拦截器
axios.interceptors.response.use(response => {
    return response
}, error => {
    return Promise.reject(error)
})


// 1、登录
export const login = (username, password) => axios.post(
    '/login',
    {
        username,
        password
    }
)

// 2、注册
export const registered = (user, password, email) => axios.post(
    '/registered',
    {
        user,
        password,
        email
    }
)

// 3、获取主页的表格数据
export const getGraphData = (params) => axios.get(
    '/home/graph',
    {
        params
    }
)
// 4、主页的历史记录
export const getHistory = (params) => axios.get(
    '/home/history',
    {
        params
    }
)

// 5、主页的用户
export const getUser = (params) => axios.get(
    '/home/user',
    {
        params
    }
)



// 6、目标提取
export const getTargetExtraction = (file, params) => axios.post(
    '/targetextraction/img',
    file,
    {
        params
    }
)
export const TargetExtractionExanple = () => axios.get('/targetextraction/example')




// 7、目标检测
export const getTargetDetection = (file, params) => axios.post(
    '/targetdetection/img',
    file,
    {
        params
    }
)
export const TargetDetectionExample = () => axios.get('/targetdetection/example')



// 8、地物分类
export const getTerrainClassification = (file, params) => axios.post(
    '/terrainclassification/img',
    file,
    {
        params
    }
)
export const TerrainClassificationExample = () => axios.get('/terrainclassification/example')



// 9变化检测 发送第一张图片
export const sedChangeBeforeImg = (file, progress, params) => {
    return axios.post(
        '/changedetection/before', 
        file, 
        {
            // headers: { "Content-Type": "multipart/form-data" },
            onDownloadProgress: progress,
            params
        }
    )
}
// 9变化检测 发送第二张图片
export const sedChangeAfterImg = (file, progress, params) => {
    return axios.post(
        '/changedetection/after',
        file,
        {
            // headers: { "Content-Type": "multipart/form-data" },
            onDownloadProgress: progress,
            params
        }
    )
}
// 9开始变化检测
export const startDetection = (params) => {
    return axios.get(
        '/changedetection/detection',
        {
            params,
            // onDownloadProgress: progress
        }
    )
}

export const changedetectionExample = () => axios.get('/changedetection/example')






// 相关api

// 1主页  获取主页的历史数据
// export const getHistoryData = () => axios.get('/home/history')
// 获取主页的表格数据
// export const getTableData = () => axios.get('/home/graph')

// 2目标提取

// // 3变化检测 发送第一张图片
// export const sedChangeBeforeImg = (file, progress, params) => {
//     return axios.post(
//         '/changedetection/before', 
//         file, 
//         {
//             // headers: { "Content-Type": "multipart/form-data" },
//             onDownloadProgress: progress,
//             params
//         }
//     )
// }
// // 变化检测 发送第二张图片
// export const sedChangeAfterImg = (file, progress, params) => {
//     return axios.post(
//         '/changedetection/after',
//         file,
//         {
//             // headers: { "Content-Type": "multipart/form-data" },
//             onDownloadProgress: progress,
//             params
//         }
//     )
// }
// // 开始变化检测
// export const startDetection = (params, progress) => {
//     return axios.get(
//         '/changedetection/detection',
//         {
//             params,
//             onDownloadProgress: progress
//         }
//     )
// }

// 4目标检测

// 5地物分类




/**
 * 所需 api
 * 1、目标提取
 *   
 * 
 * 2、变化检测
 *  1)上传第一张图片
 *    post请求        /changedetection/before/:id    
 *        我会上传一张图片和一个id代表这张图片的唯一标识
 *  2)上传第二张图片
 *    post请求         /changedetection/after/:id
 *        我会上传一张图片和一个id代表这张图片的唯一标识
 *  3) 开始检测
 *    get请求        /changedetection/detection/:id1/:id2/
 *        当我发送这个请求你在开始检测，id1和id2就是上面传的需要检测的两张图片，
 *        每次你就检测这两张就行了，防止我前端中重新上传，然后保存相关数据
 *     返回 jsonge格式的数据 
 *      {
 *          url: 'dkfkdfkfjkdfj',
 *          要扩展的数据，比如我们之前说的机损所有发生变化的个数等
 *      }
 * 
 * 
 * 3、目标加测
 * 
 * 
 * 4、地物分类
 * 
 * 
 * 
 * 5、主页的历史数据
 *   get请求    /home/history
 *    返回数据 json 
 *   {
 *      id: 12,
 *      label: '变化检测',
 *      time: '2020,2020fgfg',
 *      title: '变化87出的开发贷款复健科',
 *   }
 *   
 * 
 * 
 * 
 * 6、主页的表格数据
 *    get请求  /home/graph
 *    返回json    最近半个月对变化检测和地物分类这两个子功能的
 *               使用情况，比如每天的使用次数，你自己看着办
 *   {
 *      变化检测: [
 *          15天每天的次数
 *      ],
 *      地物分类: [
 *          15天每天的次数
 *      ],
 *   }
 *   
 */
