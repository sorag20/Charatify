import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Kekka.module.css";
const Kekka = () => {
  const navigate = useNavigate();

  const onHttpsapplottiefilescomanImageClick = useCallback(() => {
    navigate("/shindan");
  }, [navigate]);

  return (
    <div className={styles.kekka}>
      <img className={styles.kekkaIcon} alt="" src="/kekka@2x.png" />
      <div className={styles.yourSongIs}>your song is.......</div>
      <img
        className={styles.httpsapplottiefilescomanIcon}
        alt=""
        src="/httpsapplottiefilescomanimation717271c50468437481a4de9c96120b81@2x.png"
        onClick={onHttpsapplottiefilescomanImageClick}
      />
      <div className={styles.playAgain}>Play again!</div>
    </div>
  );
};

export default Kekka;
