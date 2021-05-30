import React from "react"

import './user-card.css';

const UserReactionCard = (props) => {
    const {imageUrl, message, time} = props

    return (
        <div className="tweet-body">
            <div className="inner-body">
                <img src={imageUrl} alt="img" className="picture" />
                <div className="body">
                    <div className="inner-body">
                        <div className="tweet">
                            {message} - {time}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default UserReactionCard
