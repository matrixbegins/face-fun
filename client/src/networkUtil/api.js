
const API_URL = "https://6orjixc7e9.execute-api.ap-south-1.amazonaws.com/main/face_upload"


const postImage = (image) =>  {
    // console.log("==========image=== ", image)
    if (!image){
        return Promise.resolve({
            image_url: "https://d2fp043e7v1132.cloudfront.net/user-images/site-icon.jpg",
            message: "Welcome! lets begin.",
            timestamp: Date.now()
        })
    }

    const options = {
        method: 'POST',
        body: image,
        headers: {
            // "Content-Type": "image/jpeg",
            "Content-Type": "multipart/form-data",
            "ff-api-key": "D3U3DNGD6C"
        }
    };


    return fetch(API_URL, options)
            .then((response) => {
                return response.json()
            })
            .then((jsonObject) => {
                console.log("API response", jsonObject)
                return jsonObject
            })
            .catch((error) => {
                console.log("API ERROR:: ", error )
            });

}

export default postImage