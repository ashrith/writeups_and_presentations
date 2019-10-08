class ExampleLogTransformer(CustomTransformer):
        _regression = True
            _binary = True
                _multiclass = True
                    _numeric_output = True
                        _is_reproducible = True
                            _excluded_model_classes = ['tensorflow']
                                _modules_needed_by_name = ["custom_package==1.0.0"]

                                    @staticmethod
                                        def do_acceptance_test():
                                                return True

                                                @staticmethod
                                                    def get_default_properties():
                                                            return dict(col_type = "numeric", min_cols = 1, max_cols = 1, relative_importance = 1)

                                                            def fit_transform(self, X: dt.Frame, y: np.array = None):
                                                                        X_pandas = X.to_pandas()
                                                                                X_p_log = np.log10(X_pandas)
                                                                                        return X_p_log

                                                                                        def transform(self, X: dt.Frame):
                                                                                                    X_pandas = X.to_pandas()
                                                                                                            X_p_log = np.log10(X_pandas)
                                                                                                                    return X_p_log

