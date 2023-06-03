import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Shindan.module.css";
const Shindan = () => {
  const navigate = useNavigate();

  const onHttpsapplottiefilescomanImageClick = useCallback(() => {
    navigate("/kekka");
  }, [navigate]);

  return (
    <div className={styles.shindan}>
      <img className={styles.folderIcon} alt="" src="/folder@2x.png" />
      <img className={styles.shindanChild} alt="" src="/rectangle-6.svg" />
      <div className={styles.goResult}>Go result</div>
      <img
        className={styles.httpsapplottiefilescomanIcon}
        alt=""
        src="/httpsapplottiefilescomanimationaf9e377f5d3c4f7eb66d2bd2716e3cab@2x.png"
        onClick={onHttpsapplottiefilescomanImageClick}
      />
      <img className={styles.headphonesIcon} alt="" src="/headphones@2x.png" />
      <div className={styles.questions}>Questions</div>
    </div>
  );
};

export default Shindan;
