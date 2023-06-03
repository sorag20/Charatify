import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./TopPage.module.css";
const TopPage = () => {
  const navigate = useNavigate();

  const onHttpsapplottiefilescomanImageClick = useCallback(() => {
    navigate("/shindan");
  }, [navigate]);

  return (
    <div className={styles.topPage}>
      <img className={styles.rectangleIcon} alt="" src="/rectangle@2x.png" />
      <div className={styles.letsPlay}>Let’s play!</div>
      <div className={styles.charatify}>Charatify</div>
      <div className={styles.cibspotify} />
      <img className={styles.vectorIcon} alt="" src="/vector.svg" />
      <img
        className={styles.httpsapplottiefilescomanIcon}
        alt=""
        src="/httpsapplottiefilescomanimation975fb9d697ea4e7da1b7ed243168cde4@2x.png"
        onClick={onHttpsapplottiefilescomanImageClick}
      />
    </div>
  );
};

export default TopPage;
