
const API_URL = "https://6orjixc7e9.execute-api.ap-south-1.amazonaws.com/main/face_upload"


const postImage = (image) =>  {
    console.log("==========image=== ", image)
    const options = {
        method: 'POST',
        data: image,
        headers: {
            "Content-Type": "image/jpeg",
            "ff-api-key": "D3U3DNGD6C"
        }
    };

    // return Promise.resolve({
    //     img_url: "https://d2fp043e7v1132.cloudfront.net/thumbnails/bChTbCFyXty5BjFxXmx8GJ.jpg",
    //     message: "Welcome! lets begin.",
    //     timestamp: Date.now()
    // })

    return fetch(API_URL, options)
            .then((response) => {
                return response.json()
            })
            .then((jsonObject) => {
                console.log("API response", jsonObject)
                // return jsonObject
            })
            .catch((error) => {
                console.log("API ERROR:: ", )
            });

}

export default postImage