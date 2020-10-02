import { useLocation } from "react-router-dom";
import useQuery from "./useQuery";

export default function useNext(default_) {
    const location = useLocation();
    const query = useQuery();
    const next = query.get('next');
    default_ = default_ || location;
    return next ? { pathname: next } : default_;
}