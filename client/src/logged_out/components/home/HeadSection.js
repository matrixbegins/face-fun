import React, { Fragment, useEffect, useState } from "react";
import PropTypes from "prop-types";
import classNames from "classnames";
import {
  Grid,
  Card,
  Box,
  withStyles,
  withWidth
} from "@material-ui/core";
import WaveBorder from "../../../shared/components/WaveBorder";
import UserReactionCard from "./userReactionCard";

import WebcamCapture from "../webcamCapture"
import postImage from "../../../networkUtil/api";

const styles = (theme) => ({
  extraLargeButtonLabel: {
    fontSize: theme.typography.body1.fontSize,
    [theme.breakpoints.up("sm")]: {
      fontSize: theme.typography.h6.fontSize,
    },
  },
  extraLargeButton: {
    paddingTop: theme.spacing(1.5),
    paddingBottom: theme.spacing(1.5),
    [theme.breakpoints.up("xs")]: {
      paddingTop: theme.spacing(1),
      paddingBottom: theme.spacing(1),
    },
    [theme.breakpoints.up("lg")]: {
      paddingTop: theme.spacing(2),
      paddingBottom: theme.spacing(2),
    },
  },
  card: {
    boxShadow: theme.shadows[4],
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
    [theme.breakpoints.up("xs")]: {
      paddingTop: theme.spacing(3),
      paddingBottom: theme.spacing(3),
    },
    [theme.breakpoints.up("sm")]: {
      paddingTop: theme.spacing(5),
      paddingBottom: theme.spacing(5),
      paddingLeft: theme.spacing(4),
      paddingRight: theme.spacing(4),
    },
    [theme.breakpoints.up("md")]: {
      paddingTop: theme.spacing(5.5),
      paddingBottom: theme.spacing(5.5),
      paddingLeft: theme.spacing(5),
      paddingRight: theme.spacing(5),
    },
    [theme.breakpoints.up("lg")]: {
      paddingTop: theme.spacing(6),
      paddingBottom: theme.spacing(6),
      paddingLeft: theme.spacing(6),
      paddingRight: theme.spacing(6),
    },
    [theme.breakpoints.down("lg")]: {
      width: "auto",
    },
  },
  wrapper: {
    position: "relative",
    backgroundColor: theme.palette.secondary.main,
    paddingBottom: theme.spacing(2),
  },
  image: {
    maxWidth: "100%",
    verticalAlign: "middle",
    borderRadius: theme.shape.borderRadius,
    boxShadow: theme.shadows[4],
  },
  container: {
    marginBottom: theme.spacing(12),
    [theme.breakpoints.down("md")]: {
      marginBottom: theme.spacing(9),
    },
    [theme.breakpoints.down("sm")]: {
      marginBottom: theme.spacing(6),
    },
    [theme.breakpoints.down("sm")]: {
      marginBottom: theme.spacing(3),
    },
  },
  containerFix: {
    [theme.breakpoints.up("md")]: {
      maxWidth: "none !important",
    },
  },
  waveBorder: {
    paddingTop: theme.spacing(4),
  },

  gridSidebar: {
    "max-height": "900px",
    "min-height": "570px"
  }
});

function HeadSection(props) {
  const { classes, theme, width, imageBody } = props;
  const [apiData, setApiData] = useState([])
  const [imageSource, setImageSource] = useState(null)
  useEffect(() => {
    postImage(imageSource).then(jsonObj => {
      const newApiData = apiData.concat(jsonObj)
      setApiData(newApiData)
    })

  }, [imageSource]);


  return (
    <Fragment>

    <div className={classNames("lg-p-top", classes.wrapper)}>
      <div className={classNames("container-fluid", classes.container)}>
      <Grid container spacing={2}>
        <Grid item xs={8} md={8}>
          <Card
            className={classes.card}
            data-aos-delay="200"
            data-aos="zoom-in"
          >
            <Box>
              <WebcamCapture setImageSource={setImageSource} />
            </Box>
          </Card>
        </Grid>

        <Grid item xs={4} md={4}>
          <Card
            className={classNames(classes.gridSidebar, classes.card)}
            data-aos-delay="200"
            data-aos="zoom-in"
          >

            {
              apiData.filter(item => !!item ).map(item => {
               return (<Box key={item.timestamp}>
                  <UserReactionCard imageUrl={item.image_url}
                    message={item.message}
                    time={item.timestamp} />
                </Box>)
              })
            }

          </Card>
        </Grid>

      </Grid>
      </div>
    </div>

      <WaveBorder
        upperColor={theme.palette.secondary.main}
        lowerColor="#FFFFFF"
        className={classes.waveBorder}
        animationNegativeDelay={2}
      />
    </Fragment>
  );
}

HeadSection.propTypes = {
  classes: PropTypes.object,
  width: PropTypes.string,
  theme: PropTypes.object,
};

export default withWidth()(
  withStyles(styles, { withTheme: true })(HeadSection)
);
