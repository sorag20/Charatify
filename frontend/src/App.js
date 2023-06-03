import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import TopPage from "./pages/TopPage";
import Kekka from "./pages/Kekka";
import Shindan from "./pages/Shindan";
import ExportToCodeErrorsDelete from "./pages/ExportToCodeErrorsDelete";
import { useEffect } from "react";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/kekka":
        title = "";
        metaDescription = "";
        break;
      case "/shindan":
        title = "";
        metaDescription = "";
        break;
      case "/export-to-code-errors-delete-me-anytime":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<TopPage />} />
      <Route path="/kekka1" element={<Kekka />} />
      <Route path="/shindan" element={<Shindan />} />
      <Route
        path="/export-to-code-errors-delete-me-anytime"
        element={<ExportToCodeErrorsDelete />}
      />
    </Routes>
  );
}
export default App;
