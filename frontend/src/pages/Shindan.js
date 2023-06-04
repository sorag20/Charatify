import React, { useState } from "react";
import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Shindan.module.css";

const questions = [
  {
    question: "① 音楽を聴くときはリラックスしたいときに聴きますか？",
    options: ["YES", "NO"],
  },
  {
    question: "② コンサートやフェスティバルに行くのが好きですか？",
    options: ["YES", "NO"],
  },
  {
    question: "③ 普段あなたは色んな人とお話をしますか？",
    options: ["YES", "NO"],
  },
  {
    question: "④ 仕事をするうえで，あなたは情熱的ですか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑤ 何か失敗した時，すぐに立ち直って元に戻ることができますか？",
    options: ["YES", "NO"],
  },
  {
    question:
      "⑥ 人と仕事をするうえで，役割を理解し，相互に助け合うことができますか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑦ 人に興味を持ち共感・信頼することができますか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑧ 意見を主張し，チームを高めることができますか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑨ 機械音が好きですか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑩ リズムに合わせてダンスしたいですか？",
    options: ["YES", "NO"],
  },
  {
    question: "⑪ 好きな音楽を通じて感じる主な感情は何ですか？",
    options: ["楽しさと活力", "情熱と刺激", "平穏と安らぎ"],
  },
];

const Shindan = () => {
  const navigate = useNavigate();
  const [answers, setAnswers] = useState(Array(questions.length).fill(null));

  const onAnswerChange = useCallback(
    (index, option) => {
      const newAnswers = [...answers];
      newAnswers[index] = option;
      setAnswers(newAnswers);
    },
    [answers]
  );

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
      <div className={styles.questionsContainer}>
        {questions.map((q, index) => (
          <div key={index} className={styles.question}>
            <h2>{q.question}</h2>
            <div className={styles.optionsContainer}>
              {q.options.map((option, optionIndex) => (
                <div key={optionIndex} className={styles.option}>
                  <input
                    type="checkbox"
                    checked={answers[index] === option}
                    onChange={() => onAnswerChange(index, option)}
                  />
                  {option}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Shindan;
