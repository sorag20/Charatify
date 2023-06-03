import styles from "./Kekka.module.css";
const Kekka = () => {
  return (
    <div className={styles.kekka}>
      <img className={styles.kekkaIcon} alt="" src="/kekka@2x.png" />
      <div className={styles.yourSongIs}>your song is.......</div>
    </div>
  );
};

export default Kekka;
