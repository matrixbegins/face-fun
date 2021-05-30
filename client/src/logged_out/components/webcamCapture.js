import React from "react"
import Webcam from "react-webcam"
import Button from '@material-ui/core/Button';
import { PlayArrow, Cancel } from '@material-ui/icons';


const WebcamCapture = (props) => {
    const {setImageSource} = props
    const webcamRef = React.useRef(null);
    const [imgSrc] = React.useState(null);

    const captureUserImage = () => {
      const imageSrc = webcamRef.current.getScreenshot();
      // setImgSrc(imageSrc);
      setImageSource(imageSrc)
    }
    let startTime = 0

    const capture = React.useCallback(() => {
      // init param
      if(startTime < 1) {
        startTime = Date.now()
      }

      const intervalId = setInterval(() => {
          if((Date.now() - startTime) > 20000){
            // time limit is over
            console.log("============== time is over clearing the interval")
            clearInterval(intervalId)
            startTime = 0
          }
          console.log("capturing the image.....")
          captureUserImage(webcamRef)
        }, 5000)

    }, [webcamRef])


    const videoConstraints = {
      width: 1280,
      height: 720,
      facingMode: "user"
    };


    return (
      <>
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width="100%"
          videoConstraints={videoConstraints}
        />
        <br/><br/>
        <Button
          variant="contained"
          color="primary"
          size="large"
          startIcon={<PlayArrow />}
          onClick={capture}
        >Let's Start</Button>

      </>
    );
  };

  export default WebcamCapture
