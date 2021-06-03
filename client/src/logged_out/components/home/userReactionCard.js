import React from "react"

import './user-card.css';

const UserReactionCard = (props) => {
    const {imageUrl, message, time} = props

    // console.log("imageUrl::", imageUrl)

    return (
        <div className="tweet-body">
            <div className="inner-body">
                <img src={imageUrl} alt="img" className="picture" />
                <div className="body">
                    <div className="inner-body">
                        <div className="tweet">
                            <strong>{message}</strong>
                            <br/>
                            <br/>
                            <i>{time}</i>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    )
}

export default UserReactionCard
