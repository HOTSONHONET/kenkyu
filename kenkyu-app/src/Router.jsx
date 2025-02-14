import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./Pages/Main";

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<Main/>} />
                <Route exact path="*" element={<Main />} />
            </Routes>
        </BrowserRouter>
    )
}

export default AppRoutes
